import React, {Component} from 'react'
import APIService from "../APIservice";
import UserForm from "./UserForm";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import {useHistory} from "react-router-dom";

const LoginView = () => {
    const apiService = new APIService();
    const history = useHistory();

    const login = (username, password) => {
        apiService.login(username, password).then(() => {
            history.push("/mycourses")
        });
    }

    return (
        <div>
            <UserForm headerText="Вход"
                      buttonText="Войти"
                      handleSubmit={login}/>
            <Grid container justify="center">
                <Grid item>
                    <Link href="/signup" variant="body2">
                        Зарегистрироваться
                    </Link>
                </Grid>
            </Grid>
        </div>
    )
}


export default LoginView
