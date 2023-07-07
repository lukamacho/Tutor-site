import { BrowserRouter } from 'react-router-dom';
import HeaderMenu from './Components/HeaderMenu';
import { Routes, Route } from 'react-router-dom';
import { theme } from './Components/Theme';
import { ThemeProvider } from '@mui/material';
import Homepage from './Pages/Homepage';
import LogIn from './Pages/LogIn';
import SignUp from './Pages/SignUp';
import { useToken } from './Components/TokenAuthentication';
import AboutUs from './Pages/AboutUs';
import Verification from './Pages/Verification';
import Admin from './Pages/Admin';
import Student from './Pages/Student';
import TutorProfile from './Pages/Tutor';
import Courses from './Pages/Courses';
import Tutors from './Pages/Tutors';
import PublicTutor from './Pages/PublicTutor';

export default function App() {
  const {token, setToken} = useToken();

  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <HeaderMenu token={token}/>
        <Routes>
          <Route path="/" element={<Homepage/>} />
          <Route path="login" element={<LogIn setToken={setToken}/>} />
          <Route path="registration" element={<SignUp setToken={setToken}/>} />
          <Route path="verification" element={<Verification setToken={setToken}/>} />
          <Route path="about" element={<AboutUs />} />
          <Route path="admin" element={<Admin />} />
          <Route path="student_profile" element={<Student token={token}/>} />
          <Route path="tutor_profile" element={<TutorProfile token={token}/>} />
          <Route path="courses" element={<Courses />} />
          <Route path="tutors" element={<Tutors />} />
          <Route path="tutors/tutor/:email" element={<PublicTutor />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}