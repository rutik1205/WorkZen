import fitz
import time
import os
from multiprocessing import Process, Queue, cpu_count


PDF = r"C:\Users\rutuj\OneDrive\Desktop\8942352036030092026.pdf"

# Number of password checks per worker
TESTS_PER_WORKER = 10_000

# Automatically use CPU cores minus one
WORKERS = max(1, cpu_count() - 1)


def benchmark_worker(pdf_path, worker_id, tests, queue):

    doc = fitz.open(pdf_path)

    if not doc.needs_pass:
        queue.put(("NOT_ENCRYPTED", worker_id))
        doc.close()
        return

    # Different invalid passwords.
    # We're measuring authentication speed, not finding the password.
    passwords = [
        f"{i:011d}"
        for i in range(
            worker_id * tests,
            (worker_id + 1) * tests
        )
    ]

    start = time.perf_counter()

    successful = 0

    for password in passwords:

        try:
            if doc.authenticate(password):
                successful += 1
        except Exception:
            pass

    elapsed = time.perf_counter() - start

    rate = tests / elapsed

    queue.put((
        "RESULT",
        worker_id,
        tests,
        elapsed,
        rate,
        successful
    ))

    doc.close()


def main():

    print("=" * 65)
    print("PDF PASSWORD VERIFICATION BENCHMARK")
    print("=" * 65)

    if not os.path.exists(PDF):
        print("\nPDF not found:")
        print(PDF)
        return

    print(f"\nPDF: {PDF}")
    print(f"CPU threads: {cpu_count()}")
    print(f"Workers: {WORKERS}")
    print(f"Tests per worker: {TESTS_PER_WORKER:,}")

    print("\nOpening PDF...")

    test_doc = fitz.open(PDF)

    if not test_doc.needs_pass:
        print("\nPDF is not password protected.")
        test_doc.close()
        return

    print("PDF is password protected.")

    test_doc.close()

    print("\nStarting benchmark...")
    print("Don't run other heavy programs during this test.\n")

    queue = Queue()
    processes = []

    total_tests = TESTS_PER_WORKER * WORKERS

    overall_start = time.perf_counter()

    for worker_id in range(WORKERS):

        p = Process(
            target=benchmark_worker,
            args=(
                PDF,
                worker_id,
                TESTS_PER_WORKER,
                queue
            )
        )

        p.start()
        processes.append(p)

    results = []

    for _ in processes:

        result = queue.get()

        results.append(result)

    for p in processes:
        p.join()

    overall_elapsed = (
        time.perf_counter()
        - overall_start
    )

    print("=" * 65)
    print("WORKER RESULTS")
    print("=" * 65)

    total_completed = 0

    for result in results:

        if result[0] != "RESULT":
            print(result)
            continue

        _, worker_id, tests, elapsed, rate, successful = result

        total_completed += tests

        print(
            f"Worker {worker_id:2d}: "
            f"{rate:,.0f} checks/sec "
            f"({tests:,} checks in {elapsed:.2f}s)"
        )

    combined_rate = (
        total_completed / overall_elapsed
    )

    print()
    print("=" * 65)
    print("FINAL BENCHMARK")
    print("=" * 65)

    print(f"\nTotal checks:")
    print(f"{total_completed:,}")

    print(f"\nTotal time:")
    print(f"{overall_elapsed:.2f} seconds")

    print(f"\nCOMBINED SPEED:")
    print(f"{combined_rate:,.0f} password checks/sec")

    # --------------------------------------------------------
    # Estimate full 11-digit search
    # --------------------------------------------------------

    TOTAL = 100_000_000_000

    worst_seconds = TOTAL / combined_rate
    average_seconds = worst_seconds / 2

    def format_time(seconds):

        days = int(seconds // 86400)
        seconds %= 86400

        hours = int(seconds // 3600)
        seconds %= 3600

        minutes = int(seconds // 60)
        seconds = int(seconds % 60)

        return (
            f"{days:,} days, "
            f"{hours} hours, "
            f"{minutes} minutes, "
            f"{seconds} seconds"
        )

    print()
    print("=" * 65)
    print("11-DIGIT SEARCH ESTIMATE")
    print("=" * 65)

    print(
        f"\nWorst case:"
    )

    print(
        format_time(worst_seconds)
    )

    print(
        f"\nAverage case:"
    )

    print(
        format_time(average_seconds)
    )

    print()
    print("=" * 65)


if __name__ == "__main__":
    main()