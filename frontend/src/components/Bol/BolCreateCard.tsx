import {
    Card,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card.tsx"

export function BolCreateCard({ children }: { children: React.ReactNode }) {
    return (
        <Card className="w-[350px]">
            <CardHeader>
                <CardTitle>Create bill of lading</CardTitle>
                <CardDescription>Deploy your new project in one-click.</CardDescription>
            </CardHeader>
            {children}
        </Card>
    )
}