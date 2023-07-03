import backgroundImage from '../Images/SignUpBG.png';
import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import { useState } from 'react';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import Button from '@mui/material/Button';
import { useNavigate } from 'react-router-dom';

export const background = {
  backgroundImage: `url(${backgroundImage})`,
  backgroundSize: 'cover',
  backgroundRepeat: 'repeat',
  backgroundPosition: 'center',
  minHeight: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

export const StyledBox = styled(Box)(({ theme }) => ({
  alignItems: 'center',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
  borderRadius: '14px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.2)',
  display: 'flex',
  flexDirection: 'column',
  height: 580,
  justifyContent: 'center',
  margin: 'auto',
  marginTop: 20,
  width: 400,
  padding: 25,
}));

const SignUp = () => {
  const navigate = useNavigate();

  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isStudent, setIsStudent] = useState(true);
  const [registeredUser, setRegisteredUser] = useState(false)

  const handleSignUp = async (e) => {
    e.preventDefault();

    const data = {
      "first_name": firstName,
      "last_name": lastName,
      "mail": email,
      "password": password,
      "is_student": isStudent,
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
            is_student: isStudent,
            first_name: firstName,
            last_name: lastName,
            password,
          }
        });
      } else {
        console.log(result);
        setRegisteredUser(true);
      }
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div style={background}>
      <StyledBox>
        <Avatar sx={{ m: 1, bgcolor: 'customColors.darkPurple', }}>
          <ExitToAppIcon />
        </Avatar>
        <Typography component="h1" variant="h5" sx={{ m: 1.5 }}>
          New Account
        </Typography>
        <TextField
          id="first-name"
          fullWidth
          label="First Name"
          margin="normal"
          name="first-name"
          onChange={e => setFirstName(e.target.value)}
          required
          autoFocus
          value={firstName}
        />
        <TextField
          id="last-name"
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
        <FormControl
          component="fieldset"
          sx={{ display: 'flex', m: 1, }}
        >
          <RadioGroup
            aria-label="option"
            name="option"
            value={isStudent? "s" : "t"}
            onChange={e => setIsStudent(e.target.value === "s" ? true : false)}
            sx={{ flexDirection: 'row', justifyContent: 'center', }}
          >
            <FormControlLabel
              value="s"
              control={<Radio />}
              label="Student"
            />
            <FormControlLabel
              value="t"
              control={<Radio />}
              label="Tutor"
            />
          </RadioGroup>
        </FormControl>
        <Button
          onClick={(e) => handleSignUp(e)}
          sx={{ margin: 1, backgroundColor: 'customColors.peachPuff', }}
          variant="outlined"
          size="large"
        >
          Sign Up
        </Button>
        {registeredUser && (
          <Typography variant="body1" color="error" sx={{ m: 1, }}>
            User with this email is already registered!
          </Typography>
        )}
      </StyledBox>
    </div>
  );
}

export default SignUp;