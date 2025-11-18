"""
MindfulAI - Main Entry Point using Google ADK
Demonstrates the complete multi-agent mental health support system built with official ADK.
"""

import os
import asyncio
from google.adk.runners import InMemoryRunner
from adk_agents import create_coordinator_agent
from adk_config import GOOGLE_API_KEY
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown


def print_header():
    """Prints the application header."""
    console = Console()

    header_text = """
    # 🧠 MindfulAI
    ## 24/7 Mental Health Crisis Support & Wellness Companion
    ### Built with Google ADK
    
    A multi-agent AI system providing intelligent mental health support with:
    - Crisis detection and immediate intervention
    - Empathetic ongoing support
    - Evidence-based coping strategies
    - Resource connection
    - Mood tracking and pattern analysis
    
    **Powered by Google ADK + Gemini 2.0 Flash**
    """

    console.print(Panel(Markdown(header_text), style="bold blue"))
    console.print(
        "\n[yellow]⚠️  Note: This is a support tool. In emergencies, call 988 or 911.[/yellow]\n"
    )


def print_instructions():
    """Prints usage instructions."""
    console = Console()
    console.print("[bold cyan]How to use MindfulAI:[/bold cyan]\n")
    console.print("1. Simply type your message or concern")
    console.print("2. The system will automatically:")
    console.print("   • Assess your needs through the Triage Agent")
    console.print("   • Detect any crisis indicators")
    console.print("   • Route you to the appropriate specialist agent")
    console.print(
        "3. You can ask for coping strategies, mood tracking, or resource help"
    )
    console.print("4. Type 'exit' or 'quit' to end the session\n")

    console.print("[bold yellow]Example prompts:[/bold yellow]")
    console.print("• 'I'm feeling really anxious about tomorrow'")
    console.print("• 'Can you help me find a therapist?'")
    console.print("• 'I'm having trouble coping with stress'")
    console.print("• 'I need someone to talk to'\n")


async def main_async():
    """Main async entry point using ADK InMemoryRunner properly."""
    # Ensure API key is set
    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not found in environment variables or .env file")
        return

    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

    # Print header and instructions
    print_header()
    print_instructions()

    # Create the coordinator agent (with all sub-agents)
    console = Console()
    console.print("[cyan]🔄 Initializing MindfulAI multi-agent system...[/cyan]")

    coordinator = create_coordinator_agent()

    # Create ADK InMemoryRunner - handles session management automatically
    runner = InMemoryRunner(agent=coordinator, app_name="agents")

    console.print("[green]✓ System ready! All agents initialized.[/green]")
    console.print("[dim]Using Google ADK InMemoryRunner for agent execution[/dim]")
    console.print("[dim]Agents: Triage → Crisis | Support | Resource[/dim]\n")
    console.print("[bold]Start your conversation below:[/bold]\n")

    # Collect all messages for run_debug
    all_messages = []

    while True:
        try:
            # Get user input
            user_input = input("\n[You]: ").strip()

            # Exit commands
            if user_input.lower() in ["exit", "quit", "q"]:
                console.print(
                    "\n[yellow]Session ended. Take care of yourself! 💙[/yellow]"
                )
                break

            if not user_input:
                continue

            # Add message to list
            all_messages.append(user_input)

            console.print("\n[bold cyan][MindfulAI]:[/bold cyan]\n")

            try:
                # Use ADK's run_debug - it handles session/history automatically
                events = await runner.run_debug(
                    user_messages=all_messages, quiet=True  # Suppress debug output
                )

                # Collect all text responses and only show the LAST one (final coordinator response)
                all_responses = []
                for event in events:
                    if hasattr(event, "content") and event.content:
                        if hasattr(event.content, "parts"):
                            for part in event.content.parts:
                                if hasattr(part, "text") and part.text:
                                    all_responses.append(part.text)

                # Display only the last response (the final coordinator output)
                if all_responses:
                    console.print(Panel(all_responses[-1], style="green"))
                else:
                    console.print(
                        "[yellow]No response received. Please try again.[/yellow]"
                    )

            except Exception as run_error:
                console.print(f"[red]Error: {str(run_error)}[/red]")
                console.print(
                    "[yellow]Please try again. If you're in crisis, call 988 immediately.[/yellow]"
                )
                # Remove failed message
                all_messages.pop()
                continue

        except KeyboardInterrupt:
            console.print("\n\n[yellow]Session interrupted. Goodbye![/yellow]")
            break
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
            console.print(
                "[yellow]Please try again. If you're in crisis, call 988 immediately.[/yellow]"
            )


def main():
    """Synchronous wrapper for the async main function."""
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n\n[yellow]Session ended. Take care of yourself! 💙[/yellow]")
    except Exception as e:
        print(f"\n[red]Error: {str(e)}[/red]")
        print(
            "\n[yellow]If you're in crisis, please call 988 (Suicide & Crisis Lifeline) immediately.[/yellow]"
        )


if __name__ == "__main__":
    main()
