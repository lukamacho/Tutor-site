import React from "react"
import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import Homepage from "./Pages/Homepage"
import Registration from "./Pages/Registration"
import Login from "./Pages/Login"

export default function App() {
    return (
        <BrowserRouter>
            <ul>
                <li><Link to="/">Homepage</Link></li>
                <li><Link to="/registration">Registration</Link></li>
                <li><Link to="/login">Login</Link></li>
            </ul>
            <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="registration" element={<Registration />} />
                <Route path="login" element={<Login />} />
            </Routes>
        </BrowserRouter>
    );
}
