import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




@CrewBase
class IntelligentVacuumCleanerQLearningSimulationCrew:
    """IntelligentVacuumCleanerQLearningSimulation crew"""

    
    @agent
    def intelligent_agent_systems_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["intelligent_agent_systems_analyst"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def reinforcement_learning_simulation_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["reinforcement_learning_simulation_specialist"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def performance_evaluation_researcher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["performance_evaluation_researcher"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def analyze_vacuum_cleaner_agent_architecture(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_vacuum_cleaner_agent_architecture"],
        )
    
    @task
    def design_q_learning_implementation(self) -> Task:
        return Task(
            config=self.tasks_config["design_q_learning_implementation"],
        )
    
    @task
    def develop_performance_evaluation_framework(self) -> Task:
        return Task(
            config=self.tasks_config["develop_performance_evaluation_framework"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the IntelligentVacuumCleanerQLearningSimulation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
