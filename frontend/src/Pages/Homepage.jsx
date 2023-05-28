import * as React from "react"
import { useState } from "react"
import AppBar from "@mui/material/AppBar"
import Box from "@mui/material/Box"
import Toolbar from "@mui/material/Toolbar"
import Typography from "@mui/material/Typography"
import Button from "@mui/material/Button"
import IconButton from "@mui/material/IconButton"
import MenuIcon from "@mui/icons-material/Menu"
import ModalDialog from "../Components/ModalDialog"

export default function Homepage() {
    const [registerOpen, setRegisterOpen] = useState(false);

    const handleRegisterOpen = () => { setRegisterOpen(true); };
    const handleRegisterClose = () => { setRegisterOpen(false); };


    const testClick = e => {
//       try {
//         const response = fetch('http://localhost:8000/admin/hello');
//
//       } catch (error) {
//         console.error('Error fetching users:', error);
//       }
      console.log(registerOpen)
    };

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static" style={{ background: '#CFCFCF' }}>
                <Toolbar>
                    <Button variant="text" sx={{ m: 0.5 }}>Homepage</Button>
                    <Button variant="text" sx={{ m: 0.5 }}>Find a Course</Button>
                    <Button variant="text" sx={{ m: 0.5 }}>Find a Teacher</Button>
                    <Button variant="contained" sx={{ m: 0.5 }} onClick={handleRegisterOpen}>Register</Button>
                    <Button variant="contained" sx={{ m: 0.5 }}>Login</Button>
                    <ModalDialog open={registerOpen} handleClose={handleRegisterClose} />
                </Toolbar>
            </AppBar>
        </Box>
    );
}
