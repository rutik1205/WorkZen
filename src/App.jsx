import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { AppLayout } from "./appLayout/appLayout"
import Home from "./pages/home"

const router = createBrowserRouter(
  [
    {
      path: "/",
      element: <AppLayout />,
      children : [
        {
          path: "/",
          element: <Home />,
        }
      ]
    }
  ]
)

const App = () => {
  return <RouterProvider router={router} />
}

export default App;