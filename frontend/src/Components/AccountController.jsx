import { Container, Box } from "@mui/material"
import Typography from "@mui/material/Typography"
import IconButton from "@mui/material/IconButton"
import { useState, useEffect } from "react"
import Avatar from "@mui/material/Avatar"
import Menu from "@mui/material/Menu"
import MenuItem from "@mui/material/MenuItem"
import Divider from "@mui/material/Divider"
import ListItemIcon from "@mui/material/ListItemIcon"
import PersonIcon from "@mui/icons-material/Person"
import Logout from "@mui/icons-material/Logout"
import { Link } from "react-router-dom"

export default function AccountController() {
  const [email, setEmail] = useState(JSON.parse(sessionStorage.getItem("email")))
  const [profileAddress, setProfileAddress] = useState("")
  const [isStudent, setIsStudent] = useState(false)
  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);

  useEffect(() => {
    const handleVerification = async () => {
      const data = {
        email: email,
      }

      console.log("/get_user/parameters")
      console.log(data)

      try {
        let response = await fetch('http://localhost:8000/get_user', {
          method: 'POST',
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        response = await response.json();
        console.log("/get_user/response");
        console.log(response)

        setProfileAddress(response.profile_address)
        setIsStudent(response.is_student)
      } catch (error) {
        console.error(error);
      }
    }

    handleVerification();
  }, []);

  const handleClick = (e) => {
    setAnchorEl(e.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleClickProfile = () => {
    console.log("handleClickProfile");
    handleClose();
  };

  const handleClickLogOut = () => {
    console.log("handleClickLogOut");

    sessionStorage.setItem("email", JSON.stringify(''));
    sessionStorage.setItem("token", JSON.stringify(''));

    handleClose();
  };

  console.log(isStudent)

  return (
    <div>
      { email !== null && (
        <Container>
          <Box
            sx={{
              alignItems: "center",
              display: "flex",
              textAlign: "center"
            }}
          >
            <IconButton
              aria-controls={open ? "account-control-menu" : undefined}
              aria-expanded={open ? "true" : undefined}
              aria-haspopup="true"
              onClick={handleClick}
              size="small"
            >
              <Avatar
                src={
                  profileAddress === null
                  ? require("../Storage/default")
                  : "../Storage/" + email
                }
                sx={{
                  height: 32,
                  width: 32
                }}
              >
              </Avatar>
            </IconButton>
          </Box>
          <Menu
            anchorEl={anchorEl}
            id="account-control-menu"
            onClick={handleClose}
            onClose={handleClose}
            open={open}
          >
            <MenuItem onClick={handleClickProfile}>
              <ListItemIcon>
                <PersonIcon fontSize="small" />
              </ListItemIcon>
              { isStudent === true
                ? (<Link to="/student_profile">My Profile</Link>)
                : (<Link to="/tutor_profile">My Profile</Link>)
              }
            </MenuItem>
            <Divider />
            <MenuItem onClick={handleClickLogOut}>
              <ListItemIcon>
                <Logout fontSize="small" />
              </ListItemIcon>
              <Link to="/">Log Out</Link>
            </MenuItem>
          </Menu>
        </Container>
      )}
    </div>
  );
}