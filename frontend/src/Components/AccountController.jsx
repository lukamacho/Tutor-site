import { Container, Box } from "@mui/material";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import { useState, useEffect } from "react";
import Avatar from "@mui/material/Avatar";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import Divider from "@mui/material/Divider";
import ListItemIcon from "@mui/material/ListItemIcon";
import PersonIcon from "@mui/icons-material/Person";
import Logout from "@mui/icons-material/Logout";
import { Link } from "react-router-dom";

export default function AccountController() {


  let profileImage =
    sessionStorage.getItem("profileImage") === "undefined"
    ? null
    : JSON.parse(sessionStorage.getItem("profileImage"));




  const [email, setEmail] = useState(JSON.parse(sessionStorage.getItem("email")));
  const [profileAddress, setProfileAddress] = useState("");
  const [isStudent, setIsStudent] = useState(false);

  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);

  useEffect(() => {
    if (email) {
      handleVerification();
    }
  }, [email]);

  const handleVerification = async () => {
    const data = {
      email: email,
    };

    try {
      let response = await fetch("http://localhost:8000/get_user", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      });

      response = await response.json();
      console.log("/get_user/response");
      console.log(response.is_student);

      setProfileAddress(response.profile_address);

      setIsStudent(response.is_student === 'True');

    } catch (error) {
      console.error(error);
    }
  };

  const handleClick = (e) => {
    setAnchorEl(e.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleClickProfile = () => {
    console.log("handleClickProfile");
    handleVerification();
    handleClose();
  };

  console.log("EHHEHHEHE")
  console.log(profileImage)

  const handleClickLogOut = () => {
    console.log("handleClickLogOut");

    setEmail(null)
    profileImage = null

    sessionStorage.setItem("email", JSON.stringify(''));
    sessionStorage.setItem("token", JSON.stringify(''));
    sessionStorage.setItem("profileImage", JSON.stringify(''));

    //sessionStorage.setItem("email", JSON.stringify(""));
    //sessionStorage.setItem("token", JSON.stringify(""));


    handleClose();

    window.location.reload();
  };

  return (
    <div>
      {email !== null && (
        <Container>
          <Box
            sx={{
              alignItems: "center",
              display: "flex",
              textAlign: "center",
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
                  profileImage === ''
                  ? require("../Storage/default")
                  : require("../Storage/" + email)
                }
                sx={{
                  height: 32,
                  width: 32,
                }}
              ></Avatar>
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
              {isStudent === true ? (
                <Link to="/student_profile">My Profile</Link>
              ) : (
                <Link to="/tutor_profile">My Profile</Link>
              )}
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
