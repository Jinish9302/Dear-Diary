import React from 'react'
import './Navbar.css'
export default function Navbar() {
  return (
    <nav className="navbar">
        <span>
            <span>Dear Diary</span>
            <ul className='navbar-list'>
              <li className='navbar-list-item'>Home</li>
              <li className='navbar-list-item'>To-Do</li>
              <li className='navbar-list-item'>Diary</li>
            </ul>
        </span>
        <span><h3>sign in</h3></span>
    </nav>
  )
}
