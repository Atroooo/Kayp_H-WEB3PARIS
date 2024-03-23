import { useEffect, useState } from 'react'
import { Layout, LayoutHeader } from './custom/Layout.tsx'
import Nav from './Nav.tsx'
import { cn } from '@/lib/utils'
import { sidebarLinks } from '@/data/SidebarLinks.tsx'

interface SidebarProps extends React.HTMLAttributes<HTMLElement> {}

export default function Sidebar2({ className }: SidebarProps) {
    const [navOpened, setNavOpened] = useState(false)

    /* Make body not scrollable when navBar is opened */
    useEffect(() => {
        if (navOpened) {
            document.body.classList.add('overflow-hidden')
        } else {
            document.body.classList.remove('overflow-hidden')
        }
    }, [navOpened])

    return (
        <aside
            className={cn(
                `left-0 right-0 top-0 z-50 w-full border-r-2 border-r-muted transition-[width] md:bottom-0 md:right-auto md:h-svh md:w-64`,
                className
            )}
        >
            {/* Overlay in mobile */}
            <div
                onClick={() => setNavOpened(false)}
                className={`absolute inset-0 transition-[opacity] delay-100 duration-700 ${navOpened ? 'h-svh opacity-50' : 'h-0 opacity-0'} w-full bg-black md:hidden`}
            />

            <Layout>
                {/* Header */}
                <LayoutHeader className='sticky top-0 justify-between px-4 py-3 shadow md:px-4'>
                    <div className={`flex items-center gap-2`}>
                        <svg
                            xmlns='http://www.w3.org/2000/svg'
                            viewBox='0 0 256 256'
                            className={`transition-all h-8 w-8}`}
                        >
                            <rect width='256' height='256' fill='none'></rect>
                            <line
                                x1='208'
                                y1='128'
                                x2='128'
                                y2='208'
                                fill='none'
                                stroke='currentColor'
                                strokeLinecap='round'
                                strokeLinejoin='round'
                                strokeWidth='16'
                            ></line>
                            <line
                                x1='192'
                                y1='40'
                                x2='40'
                                y2='192'
                                fill='none'
                                stroke='currentColor'
                                strokeLinecap='round'
                                strokeLinejoin='round'
                                strokeWidth='16'
                            ></line>
                            <span className='sr-only'>Website Name</span>
                        </svg>
                        <div
                            className={`flex flex-col justify-end truncate visible w-auto`}
                        >
                            <span className='font-medium text-left'>KAYP Admin</span>
                            <span className='text-xs text-left'>Satoshi Nakamoto #12345</span>
                        </div>
                    </div>
                </LayoutHeader>

                {/* Navigation links */}
                <Nav
                    id='sidebar-menu'
                    className={`h-full flex-1 overflow-auto ${navOpened ? 'max-h-screen' : 'max-h-0 py-0 md:max-h-screen md:py-2'}`}
                    links={sidebarLinks}
                />
            </Layout>
        </aside>
    )
}