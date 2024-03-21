"use client";
import Link from "next/link";
import React from "react";
import { Separator } from "./ui/separator";

const Header = ({ route }: { route: string }) => {
  return (
    <header>
      <title>{route}</title>
      <nav className="flex gap-3 m-5 justify-around">
        <Link href="/">Home</Link>
        <Link href="/about">About</Link>
        <Link href="/contact">Contact</Link>
        <Separator orientation="vertical" className="h-6" />
        <Link href="/login">Login</Link>
        <Link href="/signup">Signup</Link>
      </nav>
    </header>
  );
};

export default Header;
