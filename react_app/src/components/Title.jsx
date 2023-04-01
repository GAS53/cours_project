import React, { useEffect, useState } from "react"
import { Button } from "./UI/button/Button"
import { Link, Outlet } from "react-router-dom";
import Modal from "./UI/modal/Modal";
import LogIn from "./LogIn";
import { useNavigate } from "react-router-dom";
import { getUser } from "./Auth";

function Title({isVisable, togleVisable}) {
    const user = getUser()
    // доделать здесь!!!!!!!!!!
    const navigate = useNavigate();
    // useEffect(() => {
    // const is_auth = {localStorage.getItem('auth') ? true : false}
    // }, [localStorage.getItem('auth')])
    // const is_auth = false


    function logout() {
        localStorage.removeItem("auth");
        navigate("/");
    }


    return (
        <>
            <div className="container-md site-container">
                <nav className="navbar sticky-top navbar-light bg-light mb-3 border-bottom border-primary">
                    <div className="container-fluid">
                        <ul className="nav nav-pills">
                            <li className="nav-item">
                                <Link to="/" className="nav-link">Главная</Link>
                            </li>
                            {user ?
                            <div>
                                <li className="nav-item">
                                    <Link to="lk/" className="nav-link">Личный кабинет</Link> 
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link" onClick={logout} href="/" tabIndex="-1" aria-disabled="true">Выход</a>
                                </li>
                            </div>
                            :<div>
                                <li className="nav-item">
                                    <Link to="register/" className="nav-link">Регистрация</Link>
                                </li>
                                <li className="nav-item">
                                    <Link to="login/" className="nav-link">Войти</Link>
                                     {/* <Button text="Войти в систему" type="button" styles="mainButton" action={togleVisable}/> */}
                                </li>

                            </div>
                            }

                        </ul>
                    

                        <form className="d-flex">
                            <input className="form-control mr-2" type="search" placeholder="Search" aria-label="Search"></input>
                            <Button text="Поиск" type="submit" styles="mainButton" />
                        </form>

                        

                    </div>
                </nav>
                <div className="container-md mt-5 idea-list">
                    <Outlet />
                </div>
            </div>
            <Modal isVisable={isVisable}>
                <LogIn togleVisable={togleVisable}></LogIn>
            </Modal>
        </>

    )
}

export default Title;