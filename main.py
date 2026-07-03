"""
main.py

HexaFlow AI
Command Line Entry Point
"""

from graph.graph_builder import graph


def main():

    print("=" * 60)
    print("🚚 HexaFlow AI - Enterprise Supply Chain Control Tower")
    print("=" * 60)

    while True:

        query = input("\nEnter your query (or type 'exit'): ")

        if query.lower() == "exit":
            print("Exiting HexaFlow AI...")
            break

        state = {
            "user_query": query,
            "inventory": {},
            "forecast": {},
            "procurement": {},
            "risk": {},
            "logistics": {},
            "communication": {},
            "approval_status": "Approved",  # Default for CLI testing
            "logs": [],
            "final_response": ""
        }

        try:
            result = graph.invoke(state)

            print("\n========== RESULT ==========\n")

            if result.get("final_response"):
                print(result["final_response"])
            else:
                print(result)

            print("\n========== EXECUTION LOGS ==========\n")

            for log in result.get("logs", []):
                print(f"• {log}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()