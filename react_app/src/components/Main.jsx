import React, { useEffect, useState } from "react"
import axios from "axios";
import { Link, Outlet } from "react-router-dom";

import Filter from './Filter'
import Idea from "./ViewIdeaInMain";
import { getAll } from "./postService";

function Main() {
    const [ideas, setIdeas] = useState([])

    useEffect(() => {
        getAll()
            .then(res =>  {setIdeas(res.data.results)})
            .catch((error) => alert.error(error.message))

      }, [setIdeas]);
    console.log(ideas)

    if (ideas.length === 0) {return <div>Нет идей</div> }
    
    return (
        <div className="container-md mt-5 idea-list">
            <div className="row justify-content-center align-items-top">
                <Filter val={ideas}/>
                    <div className="col">
                    
                        {ideas.map(idea =>
                        
                            <Link to={`/idea/?id=${idea.id}`}>
                                <div className="page">
                                    <Idea 
                                        key={idea.preview}
                                        title={idea.title}
                                        preview={idea.preview}
                                        created={idea.created}
                                    />
                                </div>
                            </Link>    
                        )}
                    
                </div>

            </div>
        </div>
        ) 
}
export default Main