import React from "react";
import Footer from "./footer";
import Header from "./header";
import { Outlet } from "react-router-dom";

export const AppLayout = ()=>
{
    return(
        <>]
        <Header/>
        <Outlet/>
        <Footer/>
        </>
    )
}