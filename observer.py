"""观察者模式"""

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """The Subject interface declared a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event"""
        pass


class Observer(ABC):
    """The Observer interface declares the update method, used by the subject."""
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some import state and notifies observers when the state changes.
    """
    state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all subscribers,
    is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored more
    comprehensively(categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("\nSubject: attach observer to the subject")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("\nSubject: detach observer to the subject")
        self._observers.remove(observer)

    """
    The subscription management methods.
    """
    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        print("\nSubject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def do_some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject
        can really do. Subjects commonly hold some import business logic,
        that triggers a notification method whenever something import is about
        to do(or after it).
        """
        print("\nSubject: I'm doing something important.")
        self.state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self.state}")
        self.notify()


# concrete Observers react to the updates issued by the Subject they had been attached to.


class ConcreteObserverA(Observer):
    def update(self, subject: ConcreteSubject) -> None:
        if subject.state < 8:
            print("\nConcreteObserverA: react to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: ConcreteSubject) -> None:
        if subject.state > 4:
            print("\nConcreteObserverB: react to the event")


if __name__ == "__main__":
    sbj = ConcreteSubject()

    observerA = ConcreteObserverA()
    sbj.attach(observerA)

    observerB = ConcreteObserverB()
    sbj.attach(observerB)

    sbj.do_some_business_logic()
    sbj.do_some_business_logic()

    sbj.detach(observerB)

    sbj.do_some_business_logic()