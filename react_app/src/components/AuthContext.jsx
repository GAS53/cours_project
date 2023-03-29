import React, { useEffect, useState, s } from "react"


const AuthContext = React.createContext({
    isLogging: false,
    onLogout: () => {},
    onLogin: (emai, password) => {},
})



export const AuthContextProvider = (props) => {
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    useEffect(() => {
        const stredLoginInfo = localStorage.getItem('isLoggedIn')
        
    if (stredLoginInfo === '1') {
        setIsLoggedIn(true)
    }
    }, [])

    const logoutHandler = () => {
        localStorage.removerItem('idLoggendin')
        setIsLoggedIn(false)
    }

    const loginHandler = () => {
        localStorage.setItem('isLoggedIn', '1')
        setIsLoggedIn(true)
    }
    return (
        <AuthContext.Provider 
        value={{
            isLoggedIn: isLoggedIn,
            onLogout: logoutHandler,
            onLogin: loginHandler
        }}>
            {props.children}
        </AuthContext.Provider>
        )
}

export default AuthContext;