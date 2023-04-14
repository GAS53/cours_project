import React, { useEffect, useState } from "react"
import axios from "axios";
import { useSearchParams } from "react-router-dom";
import { Link } from "react-router-dom";
import { getAuth, getIdea, connectToIdea, LikeIdea } from "./postService";
import { useNavigate } from "react-router-dom";



function OneIdea() {
    const navigate = useNavigate();
    const maxios = axios.create({
        timeout: 3000, // 3 seconds
    });
    const [queryParameters] = useSearchParams()
    let idea_id = queryParameters.get('id')
    const [oneIdea, setOneIdea] = useState([])
    const [rubirc, setRubirc] = useState([])




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
        console.log('oneIdea.likesToIdea')
        console.log(oneIdea.likesToIdea)
        if (oneIdea.likesToIdea.indexOf(auth.id) != -1) {
            oneIdea.likesToIdea.push(auth.id)
            const data = {
                id: idea_id,
                user_id: auth.id
            }
            console.log('data')
            console.log(data)
            LikeIdea(data)
                .then(alert(`вы ${auth.login} лайкнули ${oneIdea.title}`))
                .catch((error) => alert(`лайк не удался ${error.message}`))

        } else {
            alert(`вы ${auth.login} уже лайкали ${oneIdea.title}`)
        }
        // window.location.reload(false)
    }

    console.log('oneIdea')
    console.log(oneIdea)


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
                                                    <strong>{rubirc.rubric}</strong>
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
                                                <div className="mt-2 d-grid gap-2">
                                                    <button type="button" className="btn btn-outline-danger">
                                                        Пожаловаться
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
                                          <h2 className="accordion-header" id="flush-headingOne">
                                            <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                                              Описание
                                            </button>
                                          </h2>
                                          <div id="flush-collapseOne" className="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                                            <div className="accordion-body">
                                                <h3>Заголовок раздела описания 1</h3>
                                                <p>
                                                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Id ad quibusdam sunt, quas iure voluptas! Odit architecto voluptates culpa eius asperiores eligendi molestias velit maiores incidunt cupiditate rerum veritatis nihil adipisci, amet nemo exercitationem mollitia. Vero rem amet iusto quod ad! Corrupti cumque distinctio vel libero repellat ex quisquam voluptas.
                                                </p>
                                                <h3>Заголовок раздела описания 2</h3>
                                                <p>
                                                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae vero tempora asperiores aspernatur alias totam ipsam eveniet, vitae, ullam, qui ad aliquid voluptatum dolorum perferendis? Dicta cum unde nulla eaque, molestiae possimus, velit maiores quasi beatae rerum quod nesciunt? Fuga qui non voluptatum expedita eligendi perspiciatis voluptatibus at adipisci, eos incidunt nobis in. Similique recusandae ut libero error tenetur distinctio mollitia aut, rem ex laborum tempore molestiae nihil delectus quam voluptatem, beatae iure voluptas quasi accusantium doloribus cum corrupti quia! Commodi quasi laborum consequuntur? Architecto ea omnis, illo nihil alias quasi qui sit facilis ipsam repellendus animi assumenda tenetur velit.                                                </p>
                                            </div>
                                          </div>
                                        </div>


                                        <div className="accordion-item">
                                          <h2 className="accordion-header" id="flush-headingTwo">
                                            <button className="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                                               {/* { oneIdea.joinUsers.length ==0 ?
                                               `Ты можешь первым присоедениться в команду`
                                              :
                                              `Уже с нами ${oneIdea.joinUsers.length} человека`} */}
                                            </button>
                                          </h2>
                                          <div id="flush-collapseTwo" className="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionFlushExample">
                                            
                                            
                                            <div className="accordion-body">
                                               <h3> Наша команда </h3>
                                               <div className="container-fluid">
                                                <div className="row justify-content-between align-items-center g-2">
                                                    
                                                    <div className="col-2">
                                                        
                                                        <p className="text-center">Laura Wright</p>
                                                    </div>

                                                    <div className="col-2">
                                            
                                                        <p className="text-center">Joseph Martinez</p>
                                                    </div>

                                                    <div className="col-2">
                                                        
                                                        <p className="text-center">Cynthia Smith</p>
                                                    </div>

                                                    <div className="col-2">
                                                        
                                                        <p className="text-center">William Walker</p>
                                                    </div>

                                                    <div className="col-2">
                                                        
                                                        <p className="text-center">Robert Franklin</p>
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
            </div>

                         
        ) 
}
export default OneIdea;