import Box from "@mui/material/Box"
import Avatar from "@mui/material/Avatar"
import ExitToAppIcon from "@mui/icons-material/ExitToApp"
import Typography from "@mui/material/Typography"
import TextField from "@mui/material/TextField"
import Button from "@mui/material/Button"
import { useState } from "react"

export default function Registration() {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    return (
        <Box
            sx={{
                alignItems: 'center',
                backgroundColor: '#F3F3F3',
                borderRadius: '14px',
                boxShadow: 2,
                display: 'flex',
                flexDirection: 'column',
                height: 500,
                justifyContent: 'center',
                margin: 'auto',
                marginTop: 10,
                width: 400,
                padding: 5,
            }}
        >
            <Avatar
                sx={{
                    backgroundColor: '#3244A8',
                    marginBottom: 2,
                }}
            >
                <ExitToAppIcon />
            </Avatar>
            <Typography
                component="h1"
                margin="normal"
                variant="h5"
            >
                Sign Up
            </Typography>
            <Box
                component="form"
            >
                <TextField
                    fullWidth
                    label="First Name"
                    margin="normal"
                    name="first-name"
                    onChange={e => setFirstName(e.target.value)}
                    required
                    value={firstName}
                />
                <TextField
                    fullWidth
                    label="Last Name"
                    margin="normal"
                    name="last-name"
                    onChange={e => setLastName(e.target.value)}
                    required
                    value={lastName}
                />
                <TextField
                    fullWidth
                    id="email"
                    label="Email Address"
                    margin="normal"
                    name="email"
                    onChange={e => setEmail(e.target.value)}
                    required
                    type="email"
                    value={email}
                />
                <TextField
                    fullWidth
                    id="password"
                    label="Password"
                    margin="normal"
                    name="password"
                    onChange={e => setPassword(e.target.value)}
                    required
                    type="password"
                    value={password}
                />
            </Box>
            <br />
            <Typography
                component="h2"
                margin="normal"
                variant="h6"
            >
                Continue As A
            </Typography>
            <div>
                <Button
                    sx={{
                        margin: 1,
                    }}
                    variant="outlined"
                >
                    Tutor
                </Button>
                <Button
                    sx={{
                        margin: 1,
                    }}
                    variant="outlined"
                >
                    Student
                </Button>
            </div>
        </Box>
    );
}
