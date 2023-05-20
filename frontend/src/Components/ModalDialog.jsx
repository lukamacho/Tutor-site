import React from "react"
import Dialog from "@mui/material/Dialog"
import Form from "./Form"

const ModalDialog = ({ open, handleClose }) => {
    return (
        <Dialog open={open} onClose={handleClose}>
            <Form handleClose={handleClose} />
        </Dialog>
    );
};

export default ModalDialog;
