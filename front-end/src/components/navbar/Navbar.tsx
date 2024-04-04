import './Navbar.css'
import { Link } from 'react-router-dom'

interface NavbarProps {
  OpenSignInBox: () => void
}


export default function Navbar(props:NavbarProps) {
  return (
    <nav className="navbar">
        <span>
            <span>Dear Diary</span>
            <ul className='navbar-list'>
              <li className='navbar-list-item'>
                <Link to='/'>Home</Link>
              </li>
              <li className='navbar-list-item'>
                <Link to='/ToDo'>ToDo</Link>
              </li>
              <li className='navbar-list-item'>
                <Link to='/Diary'>Diary</Link>
              </li>
            </ul>
        </span>
        <span><h3><button className="sign-in-btn" onClick={props.OpenSignInBox}>Sign In</button></h3></span>
    </nav>
  )
}
