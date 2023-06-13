import * as React from "react"
import { useState } from "react"
import { Link } from "react-router-dom"
import AppBar from "@mui/material/AppBar"
import Box from "@mui/material/Box"
import Toolbar from "@mui/material/Toolbar"
import Button from "@mui/material/Button"
import ModalDialog from "../Components/ModalDialog"

export default function Homepage() {
    const [registerOpen, setRegisterOpen] = useState(false);

    const handleRegisterOpen = () => { setRegisterOpen(true); };
    const handleRegisterClose = () => { setRegisterOpen(false); };

    return (
        <Box sx={{ flexGrow: 1 }}>
            <ul>
                <li><Link to="/">Homepage</Link></li>
                <li><Link to="/registration">Registration</Link></li>
                <li><Link to="/login">Login</Link></li>
            </ul>
            <AppBar position="static" style={{ background: '#CFCFCF' }}>
                <Toolbar>
                    <Button variant="text" sx={{ m: 0.5 }}>Homepage</Button>
                    <Link to="/courses" sx={{ m: 0.5 }}>Find a Course</Link>
                    <Link to="/tutors" sx={{ m: 0.5 }}>Find a Tutor</Link>
                    <Button variant="contained" sx={{ m: 0.5 }} onClick={handleRegisterOpen}>Register</Button>
                    <Button variant="contained" sx={{ m: 0.5 }}>Login</Button>
                    <ModalDialog open={registerOpen} handleClose={handleRegisterClose} />
                </Toolbar>
            </AppBar>
        </Box>
    );
}
