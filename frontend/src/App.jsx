import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Homepage from "./Pages/Homepage"
import Registration from "./Pages/Registration"
import Login from "./Pages/Login"
import Admin from "./Pages/Admin"

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="registration" element={<Registration />} />
                <Route path="login" element={<Login />} />
                <Route path="admin" element={<Admin />}/>
            </Routes>
        </BrowserRouter>
    );
}
