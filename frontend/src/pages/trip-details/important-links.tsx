import { Link2, Plus } from "lucide-react";

export function ImportantLinks() {
    return (
        <div className="space-y-6">
            <h2 className="font-semibold text-xl">Links importantes</h2>
            <div className="space-y-5">
                <div className="flex items-center justify-between gap-4">
                    <div className="space-y-1.5 flex-1">
                        <span className="block font-medium text-zinc-100">Reserva AirBnB</span>
                        <a href="#" className="block text-xs text-zinc-400 truncate hover:text-zinc-200">https://www.airbnb.com.br/rooms/104700011</a>
                    </div>
                    <a href="#">
                        <Link2 className="text-zinc-400 size-5" />
                    </a>
                </div>
            </div>
            <button className="text-zinc-200 justify-center bg-zinc-800 rounded-lg px-5 h-11 font-medium flex items-center gap-2 hover:bg-zinc-700 w-full">
                <Plus className="size-5" />
                Cadastrar novo link
            </button>
        </div>
    )
}