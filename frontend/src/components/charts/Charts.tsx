import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card.tsx";
import {Bar, BarChart, ResponsiveContainer} from "recharts";

const data = [
    {
        revenue: 10400,
        subscription: 240,
    },
    {
        revenue: 14405,
        subscription: 300,
    },
    {
        revenue: 9400,
        subscription: 200,
    },
    {
        revenue: 8200,
        subscription: 278,
    },
    {
        revenue: 7000,
        subscription: 189,
    },
    {
        revenue: 9600,
        subscription: 239,
    },
    {
        revenue: 11244,
        subscription: 278,
    },
    {
        revenue: 26475,
        subscription: 189,
    },
];

interface StatsCardProps {
    cardTitle: string;
    number: string;
    percentage: string;
}

function StatsCard({ cardTitle, number, percentage }: StatsCardProps) {
    return (
        <Card>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-base font-normal">
                    {cardTitle}
                </CardTitle>
            </CardHeader>
            <CardContent>
                <div className="text-2xl font-bold">{number}</div>
                <p className="text-xs text-muted-foreground">{percentage}</p>
                <div className="mt-4 h-[80px]">
                    <ResponsiveContainer width="100%" height="100%">
                        <BarChart data={data}>
                            <Bar
                                dataKey="subscription"
                                style={
                                    {
                                        fill: "var(--theme-primary)",
                                        opacity: 1,
                                        "--theme-primary": `hsl("red")`,
                                    } as React.CSSProperties
                                }
                            />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </CardContent>
        </Card>
    );
}

export function CardsStats() {
    return (
        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-2">
            <StatsCard
                cardTitle="Container on delivery"
                number="4503"
                percentage="+12.3% from last month"
            />
            <StatsCard
                cardTitle="Bill of lading created"
                number="23503"
                percentage="+11 from last month"
            />
        </div>
    );
}
