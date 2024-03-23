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
            <div className={"pl-10 pr-10 gap-10 flex flex-col"}>
                {children}
            </div>
        </Card>
    )
}