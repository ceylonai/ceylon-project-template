import {Card, CardContent} from "@/components/ui/card";
import {Skeleton} from "@/components/ui/skeleton";

const ChatMessages = () => {
    return <Card className="overflow-hidden w-full h-full">
        <CardContent className={"py-2"}>
            <Skeleton className="w-full h-[20px] rounded-full"/>
            <Skeleton className="w-full h-[20px] rounded-full"/>
            <Skeleton className="w-full h-[20px] rounded-full"/>
            <Skeleton className="w-full h-[20px] rounded-full"/>
        </CardContent>
    </Card>;
};

export default ChatMessages