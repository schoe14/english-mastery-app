import Link from 'next/link';

export default function Home() {
    return (
        <div>
            <h1>Home Page</h1>
            <nav>
                <ul>
                    <li><Link href="/word-of-the-day">Word of the Day</Link></li>
                    <li><Link href="/chatroom">Chatroom</Link></li>
                    <li><Link href="/writing-correction">Writing Correction</Link></li>
                    <li><Link href="/word-quiz">Word Quiz</Link></li>
                    <li><Link href="/daily-scripts">Daily Scripts</Link></li>
                </ul>
            </nav>
        </div>
    );
}
