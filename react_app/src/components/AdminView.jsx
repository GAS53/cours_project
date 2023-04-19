import React, { useEffect, useState } from "react";
import { getAllUsers } from './postService'
import UserItem from "./UserItem";
import AdminMenu from './AdminMenu';

const AdminView = (props) => {

    const [usersList, setUsers] = useState([])

    useEffect(() => {
        getAllUsers()
            .then(res => { setUsers(res.data.results) })
            .catch((error) => alert.error(error.message))

    }, [setUsers]);
    console.log('users\n', usersList)

    return (
        <div className="container-md mt-5 idea-list">
            <div className="row justify-content-center align-items-top">
                <div className="col">
                    <AdminMenu/>
                </div>
            </div>
        </div>
    )

}

export default AdminView