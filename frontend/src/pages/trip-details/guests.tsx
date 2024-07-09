import { CircleDashed, UserCog } from "lucide-react";

export function Guests() {
    return (
        <div className="space-y-6">
            <h2 className="font-semibold text-xl">Convidados</h2>
            <div className="space-y-5">
                <div className="flex items-center justify-between gap-4">
                    <div className="space-y-1.5 flex-1">
                        <span className="block font-medium text-zinc-100">Nome Sobrenome</span>
                        <span className="block text-sm text-zinc-400 truncate">email@email.com</span>
                    </div>
                    <CircleDashed className="text-zinc-400 size-5" />
                </div>
            </div>
            <button className="text-zinc-200 justify-center bg-zinc-800 rounded-lg px-5 h-11 font-medium flex items-center gap-2 hover:bg-zinc-700 w-full">
                <UserCog className="size-5" />
                Gerenciar convidados
            </button>
        </div>
    )
}