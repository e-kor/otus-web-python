import React, {Component} from 'react'
import APIService from "../APIservice";
import UserForm from "./UserForm";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import {useHistory} from "react-router-dom";

const SignupView = () => {
    const apiService = new APIService();
    const history = useHistory();

    const register = (username, password) => {
        apiService.register(username, password).then(() => {
            history.push("/login")
        });
    }

    return (
        <div>
            <UserForm headerText="Регистрация"
                      buttonText="зарегистрироваться"
                      handleSubmit={register}/>
            <Grid container justify="center">
                <Grid item>
                    <Link href="/login" variant="body2">
                        Уже есть аккаунт?
                    </Link>
                </Grid>
            </Grid>
        </div>
    )
}







export default SignupView
