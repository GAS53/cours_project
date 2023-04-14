import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { logIn, setInLocal } from "./postService";

const LogIn = ({togleVisable}) => {
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
        const loginForm = event.currentTarget;
        if (loginForm.checkValidity() === false) {
            event.stopPropagation();
            }
        setValidated(true);
        const data = {
            email: loginForm.username.value,
            password: loginForm.password.value,
            }
        console.log('login data')
        console.log(data)
        logIn(data)
            .then((res) => {console.log('dfdfdfdgd1111111111')
                console.log(res.data)
                setInLocal(res.data)})
            .catch((err) => alert(`неверно введен email или пароль ${err.message}`))
        navigate("/")
    }





    return (
        <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
                <div className="modal-header">
                    <h5 className="modal-title" id="exampleModalLabel">Войдите в систему</h5>
                </div>
                <div className="modal-body">
                <form 
                        id="validation-form"
                        noValidate
                        validated={validated.toString()}
                        onSubmit={handleSubmit}
                        
                        >
                        <div className="mb-3">
                            <label className="form-label">Email</label>
                            <input type="email" className="form-control" id="username" aria-describedby="emailHelp"
                                placeholder="Введите логин"/>
                        </div>
                        <div className="mb-3">
                            <label className="form-label">Пароль</label>
                            <input type="password" className="form-control" id="password"
                                placeholder="Введите пароль"/>
                        </div>
                        <div className="mb-3 form-check">
                            <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
                                <label className="form-check-label">Запомнить меня</label>
                        </div>
                        <div className="modal-footer">
                            <button type="button" className="btn btn-outline-secondary"
                                data-bs-dismiss="modal" onClick={togleVisable}>Закрыть</button>
                            <button type="submit" className="btn mainButton">Войти</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
};

export default LogIn;