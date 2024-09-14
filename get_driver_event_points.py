import fastf1


def get_driver_event_points(driver_abbreviation: str, year: int, event_name: str, session_type: str) -> float:
    """
    :param driver_abbreviation: e.g. LEC for Leclerc, VER for Verstappen
    :param year: year of the event
    :param event_name: name of the event, usually country name, city name, or track name
    :param session_type: 'Race' or 'Sprint'
    :return: number of points scored by the driver on the event
    :raise: ValueError if provided driver_abbreviation and/or session_type does not exist for the provided event
    """
    valid_session_types = ["Race", "Sprint"]
    if session_type not in valid_session_types:
        raise ValueError(f"Invalid value for argument {session_type}: {session_type}\n"
                         f"Valid values are: {valid_session_types}")

    session = fastf1.get_session(year=year, gp=event_name, identifier=session_type)
    session.load()

    for driver in session.results.iloc:
        if driver.Abbreviation == driver_abbreviation:
            return driver.Points

    raise ValueError(f"No driver with abbreviation {driver_abbreviation} at this event")


if __name__ == "__main__":
    driver = "LEC"
    year = 2024
    event = "Monza"
    session = "Race"

    points_scored = get_driver_event_points(driver, year, event, session)

    print(f"{driver} scored {points_scored} points at {event} {session.lower()} in {year}.")
