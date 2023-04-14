import React, { useEffect, useState } from "react"
import { useSearchParams } from "react-router-dom";
import { Link } from "react-router-dom";
import { getAuth, getIdea, connectToIdea, LikeIdea } from "./postService";
import { useNavigate } from "react-router-dom";



function OneIdea() {
    const navigate = useNavigate();
    const [queryParameters] = useSearchParams()
    let idea_id = queryParameters.get('id')
    const [oneIdea, setOneIdea] = useState([])





    useEffect(() => {
        const auth = getAuth()
        if (auth) {
            getIdea(idea_id)
                .then(res => setOneIdea(res.data))
                .catch(res => {alert(res)})
        } else { navigate( '/welcome/') }
        },[])


    function connectHandler(e) {
        connectToIdea(idea_id)
            .then(res => {
                    alert(`вы вступили в команду ${oneIdea.title}`)
                })
            .catch((error) => {
                if (error.response.status === 423 ) {
                        alert(`вы уже состоите в команде ${oneIdea.title}`)
                    } else {
                    alert(`ошибка при добавлении пользователя  ${error.message}`)}})
        // window.location.reload(false)
    }

    function likeHandler(e) {
        const auth = getAuth()
        if (oneIdea.likesToIdea.indexOf(auth.id) === -1) {
            const data = {
                idea: idea_id,
                autor: auth.id
            }
            LikeIdea(data)
                .then(alert(`вы ${auth.login} лайкнули ${oneIdea.title}`))
                .catch((error) => {
                    if (error.response.status === 423 ) {
                        alert(`вы уже лайкали ${oneIdea.title}`)
                    } else {
                        alert(`ошибка при добавлении лайка ${error.message}`)}})

        // window.location.reload(false)
    }}

oneIdea.joinedUser is undefined


    return (
        <div className="card mb-3" style={{minHeight: '166px', minWidth: '380px'}}>
                        <div className="card-body">

                            <div className="row g-3 justify-content-left">

                                <div className="col-sm-2 card-image d-none d-md-block my-auto">
                                    
                                </div>

                                <div className="col" style={{minWidth: '340px'}}>

                                    <div className="container">
                                        <div className="row justify-content-center align-items-center g-2">
                                            <div className="col-4">
                                                <h4 className="card-title text-center">
                                                    <strong>{oneIdea.title}</strong>

                                                </h4>
                                            </div>
                                        </div>

                                        <div className="row g-1">

                                            <div className="col-4 my-auto">
                                                <Link className="nameLink" to='/' >idea</Link>
                                            </div>



                                            <div className="col-1 my-auto">
                                                <small className="text-muted">(1)</small>
                                            </div>
                                        
                                            <div className="row justify-content-center align-items-center g-2">
                                                <div className="col">
                                                    <p className="card-text">Описание</p>
                                                    <p>{oneIdea.body}</p>
                                                    <p className="card-text">
                                                        <small className="text-muted">Опубликовано {oneIdea.created}
                                                            года</small>
                                                    </p>
                                                </div>
                                            </div>

                                        </div>
                                    </div>

                                </div>

                                <div className="col-3 my-auto">
                                    <div className="container">
                                        <div className="row g-2 mx-auto justify-content-center">

                                            <div className="col">
                                                <div className="mt-2 text-center text-muted">
                                                    <strong>oneIdea.rubric.rubirc_name</strong>
                                                </div>
                                                <div className="mt-2 text-center">
                                                    <h1>⭐⭐⭐⭐⭐</h1>
                                                </div>
                                                <div className="mt-2 d-grid gap-2">
                                                    <button type="button" onClick={connectHandler} className="btn mainButton">
                                                        Вступить в команду
                                                    </button>
                                                </div>
                                                <div className="mt-2 d-grid gap-2">
                                                    <button type="button" onClick={likeHandler} className="btn btn-outline-warning">
                                                        Лайкнуть
                                                    </button>
                                                </div>

                                        </div>
                                    </div>
                                </div>

                            </div>


                            <div className="row justify-content-center align-items-center g-2">
                                <div className="col">
                                    
                                    <div className="accordion accordion-flush" id="accordionFlushExample">
                                        <div className="accordion-item">
                                          <h2 className="accordion-header" id="flush-headingTwo">
                                            <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                                               { oneIdea.joinedUser.length === 0 ?
                                               `Ты можешь первым присоедениться в команду`
                                              :
                                              `Уже с нами ${oneIdea.joinedUser.length} человека`}
                                            </button>
                                          </h2>
                                          <div id="flush-collapseTwo" className="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionFlushExample">
                                            
                                            
                                            <div className="accordion-body">
                                               <h3> Наша команда </h3>
                                               <div className="container-fluid">
                                                <div className="row justify-content-between align-items-center g-2">
                                                    {OneIdea.joinedUser.map( usr => {
                                                       <div className="col-2">
                                                            <p className="text-center">{usr.id}</p>
                                                        </div> 
                                                        })}
                                                </div>
                                               </div>
                                            </div>
                                          </div>
                                        </div>
                                        
                                      </div>

                                </div>
                                </div>
                                </div>
                                </div>
            </div>

                         
        ) 
}
export default OneIdea;