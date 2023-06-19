import { Routes, Route } from "react-router-dom"

import Homepage from "../Pages/Homepage"
import Registration from "../Pages/Registration"
import Login from "../Pages/Login"
import Admin from "../Pages/Admin"
import AboutUsPage from "../Pages/About"
import Student from "../Pages/Student"
import TutorProfile from "../Pages/Tutor"
import Courses from "../Pages/Courses"
import Tutors from "../Pages/Tutors"
import PublicTutor from "../Pages/PublicTutor"
import Verification from "../Pages/Verification"

export default function PageRouter() {
  return (
    <Routes>
      <Route path="/" element={<Homepage />} />
      <Route path="registration" element={<Registration />} />
      <Route path="login" element={<Login />} />
      <Route path="admin" element={<Admin />}/>
      <Route path="about" element={<AboutUsPage />}/>
      <Route path="student_profile" element={<Student />}/>
      <Route path="tutor_profile" element={<TutorProfile />}/>
      <Route path="courses" element={<Courses />}/>
      <Route path="tutors" element={<Tutors />}/>
      <Route path="tutors/tutor/:email" element={<PublicTutor />} />
      <Route path="verification" element={<Verification />}/>
    </Routes>
  );
}