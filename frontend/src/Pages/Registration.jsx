import Box from "@mui/material/Box"
import Avatar from "@mui/material/Avatar"
import ExitToAppIcon from "@mui/icons-material/ExitToApp"
import Typography from "@mui/material/Typography"
import TextField from "@mui/material/TextField"
import Button from "@mui/material/Button"
import { useState } from "react"
import { useNavigate} from 'react-router-dom';


export default function Registration() {
    const navigate = useNavigate();

    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [registeredUser, setRegisteredUser] = useState(false)
    const handleSignUp = async (e, is_student) => {
        e.preventDefault();

        const data = {
            "first_name": firstName,
            "last_name": lastName,
            "mail": email,
            "password": password,
            "is_student": is_student,
        }

        try {
            const response = await fetch('http://localhost:8000/sign_up', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: { 'Content-Type': 'application/json' }
            });
            const result = await response.json();

      if (result.message !== "User with this mail already exist!") {
          navigate('/verification', {
            state: {
              email,
              verificationCode: result.verificationCode,
              is_student,
              first_name: firstName,
              last_name: lastName,
              password
            }
          });
      } else {
        console.log(result)
        setRegisteredUser(true)
      }
        } catch (error) {
            console.error(error);
        }
    };

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
                    onClick={(e) => handleSignUp(e, false)}
                    sx={{
                        margin: 1,
                    }}
                    variant="outlined"
                >
                    Tutor
                </Button>
                <Button
                    onClick={(e) => handleSignUp(e, true)}
                    sx={{
                        margin: 1,
                    }}
                    variant="outlined"
                >
                    Student
                </Button>
            </div>
            </Box>
            {registeredUser && (
            <Typography variant="body1" color="error">
              User with this email is already registered.
            </Typography>
          )}
        </Box>
    );
}
