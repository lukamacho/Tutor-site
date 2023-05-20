import React, { useState } from "react"
import TextField from "@mui/material/TextField"
import Button from "@mui/material/Button"

const Form = ({ handleClose }) => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = e => {
        e.preventDefault();
        handleClose();
    };

    return (
        <form onSubmit={handleSubmit}>
            <TextField
                label="First Name"
                variant="filled"
                value={firstName}
                onChange={e => setFirstName(e.target.value)} />
            <TextField
                label="Last Name"
                variant="filled"
                value={lastName}
                onChange={e => setLastName(e.target.value)} />
            <TextField
                label="Email"
                variant="filled"
                type="email"
                value={email}
                onChange={e => setEmail(e.target.value)} />
            <TextField
                label="Password"
                variant="filled"
                type="password"
                value={password}
                onChange={e => setPassword(e.target.value)} />
            <div>
                <Button variant="contained" onClick={handleClose}>Cancel</Button>
                <Button type="submit" variant="contained" color="primary">Signup</Button>
            </div>
        </form>
    );
};

export default Form;
