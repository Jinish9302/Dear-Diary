import './Navbar.css'
import { Link } from 'react-router-dom'
export default function Navbar() {
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
        <span><h3>sign in</h3></span>
    </nav>
  )
}
