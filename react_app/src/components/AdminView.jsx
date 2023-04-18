import React, { useEffect, useState } from "react";
import { getAllUsers } from './postService'
import UserItem from "./UserItem";


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
                    <div class="container-fluid">
                        <div class="row justify-content-center align-items-center g-2">
                            <div class="col">Логин</div>
                            <div class="col">Емаил</div>
                            <div class="col">Статус</div>
                            <div class="col">Изменить статус</div>
                        </div>
                    </div>
                    <ol>
                        {usersList.map(userItem =>

                            <li>
                                <UserItem userItem={userItem} key={userItem.id} />
                            </li>
                        )}

                    </ol>
                </div>
            </div>
        </div>
    )

}

export default AdminView