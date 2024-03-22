import {
    IconBooks,
    IconDashboard, IconDeviceDesktopAnalytics, IconFileBroken, IconFileDescription,
    IconSettings,
} from '@tabler/icons-react'
import {Bell, FilePlus, FilesIcon} from "lucide-react";

export interface NavLink {
    title: string
    label?: string
    href: string
    icon: JSX.Element
}

export interface SideLink extends NavLink {
    sub?: NavLink[]
}

export const sidebarLinks: SideLink[] = [
    {
        title: 'Dashboard',
        label: '',
        href: '/',
        icon: <IconDashboard size={18} />,
    },
    {
        title: 'Document',
        label: '',
        href: '',
        icon: <IconFileDescription size={18} />,
        sub: [
            {
                title: 'Create new document',
                label: '',
                href: '/bol/create',
                icon: <FilePlus size={18} />,
            },
            {
                title: 'List of documents',
                label: '',
                href: '/bol/list',
                icon: <FilesIcon size={18} />,
            },
            {
                title: 'Draft',
                label: '',
                href: '/bol/draft',
                icon: <IconFileBroken size={18} />,
            },
        ],
    },
    {
        title: 'Activity',
        label: '',
        href: '',
        icon: <IconDeviceDesktopAnalytics size={18} />,
        sub: [
            {
                title: 'Notifications',
                label: '',
                href: '/activity/notifications',
                icon: <Bell size={18} />,
            },
            {
                title: 'History',
                label: '',
                href: '/activity/history',
                icon: <IconBooks size={18} />,
            },
        ],
    },
    {
        title: 'Settings',
        label: '',
        href: '/settings',
        icon: <IconSettings size={18} />,
    },
]