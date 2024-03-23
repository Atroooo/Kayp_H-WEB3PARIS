import {
    Card,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card.tsx"

export function PageLayout({ children, title, description }: { children: React.ReactNode, title?: string, description?: string}) {
    return (
        <Card className={"w-full"}>
            <CardHeader>
                <CardTitle>{title}</CardTitle>
                <CardDescription>{description}</CardDescription>
            </CardHeader>
            <div className={"pl-5 pr-5 gap-1 flex flex-col"}>
                {children}
            </div>
        </Card>
    )
}