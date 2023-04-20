import React, { useEffect, useState } from "react"
import { Button } from "./UI/button/Button"
import { Link, Outlet } from "react-router-dom";
import Modal from "./UI/modal/Modal";
import LogIn from "./LogIn";
import { useNavigate } from "react-router-dom";
import { logout, getAuth } from '../components/postService'

import MenuDropdown from './MenuDropdown'

function Title({isVisable, togleVisable}) {
    const user = getAuth()
    const navigate = useNavigate();
    // useEffect(() => {
    // const is_auth = {localStorage.getItem('auth') ? true : false}
    // }, [localStorage.getItem('auth')])
    // const is_auth = false

    console.log(user) 


    


    return (
        <>
            <div className="container-md site-container">
                <nav className="navbar sticky-top navbar-light bg-light mb-3 border-bottom border-primary">
                    <div className="container-fluid">
                        <ul className="nav nav-pills">
                            <li className="nav-item">
                                <Link to="/" className="nav-link">Главная</Link>
                            </li>
                            <MenuDropdown/>
                            {user ?
                            <li className="nav-item">
                                <p><strong>Вы вошли как {user.login}</strong></p>
                            </li>

                            :
                            <div>
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