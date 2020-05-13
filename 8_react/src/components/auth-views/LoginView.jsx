import React, {Component} from 'react'
import APIService from "../APIservice";
import UserForm from "./UserForm";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";


class LoginView extends Component {
    constructor(props) {
        super(props);
        this.apiService = new APIService();
    }


    render() {
        return (
            <div>
            <UserForm headerText="Вход"
                      buttonText="Войти"
                      handleSubmit={this.apiService.login}/>
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
}

export default LoginView
