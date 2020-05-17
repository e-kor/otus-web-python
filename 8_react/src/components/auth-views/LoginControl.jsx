import React from 'react';
import Nav from "react-bootstrap/Nav";
import Button from "@material-ui/core/Button";
import {useHistory} from 'react-router-dom';


const LoginControl = props => {



   {const history = useHistory();

        if (localStorage.token) {
            return <Button variant="contained" color={"default"} onClick={() => {
                localStorage.removeItem("token");
                history.push("/")
            }}>LogOut</Button>

        } else {
            return <Nav.Link href="/login">Login</Nav.Link>

        }
    }
};


export default LoginControl
