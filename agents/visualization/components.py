"""
Enhanced visual components for rich terminal output.
"""

from typing import Dict, List, Optional, Union
from rich.console import Console
from rich.table import Table
from rich.tree import Tree
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.layout import Layout
from rich.syntax import Syntax
from rich.markdown import Markdown
from datetime import datetime, timedelta

class VisualComponents:
    """Rich visual components for terminal interface."""
    
    def __init__(self):
        self.console = Console()
    
    def create_process_timeline(
        self, 
        steps: List[Dict],
        current_step: Optional[int] = None
    ) -> Tree:
        """
        Create a visual timeline of the process.
        
        Args:
            steps: List of step dictionaries with 'name' and 'status'
            current_step: Index of current step
        """
        timeline = Tree("[bold blue]Formation Process[/bold blue]")
        
        for i, step in enumerate(steps):
            if i == current_step:
                status = "🔵 [bold blue]In Progress[/bold blue]"
            elif i < current_step:
                status = "✅ [green]Complete[/green]"
            else:
                status = "⚪ Pending"
            
            timeline.add(f"{step['name']} - {status}")
        
        return timeline
    
    def create_comparison_table(
        self,
        title: str,
        headers: List[str],
        rows: List[tuple],
        highlight_column: Optional[int] = None
    ) -> Table:
        """
        Create a comparison table with optional column highlighting.
        
        Args:
            title: Table title
            headers: Column headers
            rows: Row data
            highlight_column: Index of column to highlight
        """
        table = Table(title=title)
        
        # Add columns with styling
        for i, header in enumerate(headers):
            style = "bold cyan" if i == highlight_column else None
            table.add_column(header, style=style)
        
        # Add rows
        for row in rows:
            table.add_row(*row)
        
        return table
    
    def create_cost_breakdown(
        self, costs: Dict[str, float]
    ) -> Panel:
        """
        Create a cost breakdown panel.
        
        Args:
            costs: Dictionary of cost items and amounts
        """
        total = sum(costs.values())
        
        # Format cost lines
        cost_lines = []
        for item, amount in costs.items():
            percentage = (amount / total) * 100
            cost_lines.append(
                f"{item}: ${amount:,.2f} ({percentage:.1f}%)"
            )
        
        content = "\n".join([
            "[bold blue]Cost Breakdown[/bold blue]",
            *cost_lines,
            "",
            f"[bold green]Total: ${total:,.2f}[/bold green]"
        ])
        
        return Panel.fit(content, title="Formation Costs")
    
    def create_checklist(
        self, items: List[Dict]
    ) -> Panel:
        """
        Create a checklist panel.
        
        Args:
            items: List of items with 'name' and 'complete' status
        """
        checklist = []
        for item in items:
            status = "✅" if item['complete'] else "⚪"
            checklist.append(f"{status} {item['name']}")
        
        return Panel.fit(
            "\n".join(checklist),
            title="Formation Checklist"
        )
    
    def create_progress_tracker(
        self, total_steps: int, current_step: int
    ) -> Progress:
        """
        Create a progress tracker.
        
        Args:
            total_steps: Total number of steps
            current_step: Current step number
        """
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            auto_refresh=False
        )
        
        task = progress.add_task(
            "Formation Progress",
            total=total_steps,
            completed=current_step
        )
        
        return progress
    
    def create_timeline_chart(
        self, events: List[Dict]
    ) -> Panel:
        """
        Create a timeline chart panel.
        
        Args:
            events: List of events with 'date' and 'description'
        """
        timeline = []
        for event in events:
            date = datetime.strptime(event['date'], '%Y-%m-%d')
            timeline.append(
                f"{date.strftime('%b %d')} - {event['description']}"
            )
        
        return Panel.fit(
            "\n".join(timeline),
            title="Formation Timeline"
        )
    
    def create_requirement_tree(
        self, requirements: Dict
    ) -> Tree:
        """
        Create a tree of requirements.
        
        Args:
            requirements: Nested dictionary of requirements
        """
        tree = Tree("[bold blue]Formation Requirements[/bold blue]")
        
        def add_requirements(parent, items):
            for key, value in items.items():
                if isinstance(value, dict):
                    branch = parent.add(key)
                    add_requirements(branch, value)
                else:
                    parent.add(f"{key}: {value}")
        
        add_requirements(tree, requirements)
        return tree
    
    def create_state_map(
        self, state_data: Dict[str, Dict]
    ) -> Panel:
        """
        Create a simplified ASCII state map with data.
        
        Args:
            state_data: Dictionary of state codes and their data
        """
        # Create a simple visual representation
        map_data = []
        for state, data in state_data.items():
            status = "✅" if data.get('available') else "❌"
            map_data.append(f"{state}: {status} {data.get('notes', '')}")
        
        return Panel.fit(
            "\n".join(map_data),
            title="State Availability Map"
        )
    
    def create_document_preview(
        self, content: str, language: str = "markdown"
    ) -> Panel:
        """
        Create a document preview panel.
        
        Args:
            content: Document content
            language: Syntax highlighting language
        """
        syntax = Syntax(
            content,
            language,
            theme="monokai",
            line_numbers=True
        )
        
        return Panel.fit(
            syntax,
            title="Document Preview"
        )
    
    def create_dashboard_layout(
        self, components: Dict[str, Union[Panel, Table, Tree]]
    ) -> Layout:
        """
        Create a dashboard layout with multiple components.
        
        Args:
            components: Dictionary of named components
        """
        layout = Layout()
        
        # Create main sections
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3)
        )
        
        # Split main section
        layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        # Assign components
        for name, component in components.items():
            if name in layout:
                layout[name].update(component)
        
        return layout
