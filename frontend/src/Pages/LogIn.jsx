import { styled } from '@mui/system';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import { useState } from 'react';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import backgroundImage from '../Images/LogInBG.png';
import Link from '@mui/material/Link';
import PropTypes from 'prop-types';
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
  marginTop: -100,
  padding: 25,
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  borderRadius: '8px',
  boxShadow: '0.5px 0.5px 10px rgba(0, 0, 0, 0.2)',
  backgroundColor: 'rgba(255, 255, 255, 0.8)',
  justifyContent: 'center',
}));

const handleGoogleSignIn = async () => {
  try {
    const response = await fetch('http://localhost:8000/google_sign_in', {
      method: 'GET',
    });
    const { authorization_url } = await response.json();
    window.location.href = authorization_url;
  } catch (error) {
    console.error(error);
  }
}

function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="/">
        Tutor site
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const LogIn = ({ setToken }) => {
  const navigate = useNavigate();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [authenticationSuccess, setAuthenticationSuccess] = useState(true);

  const handleSubmit = async (e) => {
  e.preventDefault();

  const data = {
    "email": email,
    "password": password,
  };

  try {
    const response = await fetch('http://localhost:8000/sign_in', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' },
    });

    const result = await response.json();
    console.log(result);
    setToken(result.token);

    if (!result.error) {
      sessionStorage.setItem('email', JSON.stringify(email));

      if (result.is_student) {
        // Student sign-in.
        navigate('/student_profile');
      } else if (result.is_admin) {
        // Admin sign-in.
        navigate('/admin');
      } else {
        // Tutor sign-in.
        navigate('/tutor_profile');
      }
    } else {
      setAuthenticationSuccess(false);
    }
  } catch (error) {
    console.error(error);
  }
};


  const handleResetPassword = async (e) => {
    e.preventDefault();

    const data = {
      "email": email,
    }

    try {
      const response = await fetch('http://localhost:8000/admin/reset_password', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
      });

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div style={background}>
      <Container component="main" maxWidth="xs">
        <StyledBox>
          <Avatar sx={{ m: 1, bgcolor: 'customColors.darkPurple', }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5" sx={{ m: 1.5 }}>
            My Account
          </Typography>
          <Box  noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <FormControlLabel
              control={<Checkbox value="remember" sx={{ color: "customColors.darkPurple" }} />}
              label="Remember Me"
            />
            <div style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              marginTop: 20,
              marginBottom: 0,
              marginLeft: 0,
              marginRight: 0, }}
            >
              <Button
                fullWidth
                type="submit"
                variant="outlined"
                sx={{ backgroundColor: 'customColors.peachPuff' }}
                onClick={(e) => handleSubmit(e)}
              >
                Log In
              </Button>
              <Button
                fullWidth
                variant="outlined"
                sx={{ backgroundColor: 'customColors.peachPuff' }}
                onClick={handleGoogleSignIn}
              >
                Sign In with Google
              </Button>
            </div>
            <Button
              fullWidth
              onClick={(e) => handleResetPassword(e)}
              sx={{ mt: 3, mb: 2, mr: 0, ml: 0, }}
              variant="outlined"
            >
              Forgot password
            </Button>
            <Link
              style={{
                display: 'flex',
                justifyContent: 'center',
                marginBottom: 10, }}
              sx={{
                color: 'customColors.darkPurple', }}
              href="/registration" variant="body2"
            >
              {"Don't Have an Account Yet? Sign Up!"}
            </Link>
            {!authenticationSuccess && (
              <Typography
                style={{
                  display: 'flex',
                  justifyContent: 'center',
                  marginBottom: 10, }}
                variant="body1"
                color="error"
              >
                Email or password is incorrect.
              </Typography>
            )}
            <Copyright/>
          </Box>
        </StyledBox>
      </Container>
    </div>
  );
}

LogIn.propTypes = {
  setToken: PropTypes.func.isRequired,
};

export default LogIn;