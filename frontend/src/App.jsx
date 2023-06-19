import React from "react"
import PageRouter from "./Components/Router"
import SidebarMenu from "./Components/SidebarMenu"
import { BrowserRouter } from "react-router-dom"

export default function App() {
  return (
    <BrowserRouter>
      <SidebarMenu />
      <PageRouter />
    </BrowserRouter>
  );
}