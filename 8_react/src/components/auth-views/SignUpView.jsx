import React, {Component} from 'react'
import APIService from "../APIservice";
import UserForm from "./UserForm";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";


class SignupView extends Component {
    constructor(props) {
        super(props);
        this.apiService = new APIService();
    }


    render() {
        return (
            <div>
            <UserForm headerText="Регистрация"
                      buttonText="зарегистрироваться"
                      handleSubmit={this.apiService.register}/>
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
}

export default SignupView
