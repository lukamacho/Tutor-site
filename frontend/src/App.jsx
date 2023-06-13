import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Homepage from "./Pages/Homepage"
import Registration from "./Pages/Registration"
import Login from "./Pages/Login"
import Admin from "./Pages/Admin"
import Student from "./Pages/Student"
import TutorProfile from "./Pages/Tutor"
import Courses from "./Pages/Courses"
import Tutors from "./Pages/Tutors"

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="registration" element={<Registration />} />
                <Route path="login" element={<Login />} />
                <Route path="admin" element={<Admin />}/>
                <Route path="student_profile" element={<Student />}/>
                <Route path="tutor_profile" element={<TutorProfile />}/>
                <Route path="courses" element={<Courses />}/>
                <Route path="tutors" element={<Tutors />}/>
            </Routes>
        </BrowserRouter>
    );
}
