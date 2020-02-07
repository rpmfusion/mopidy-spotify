%global srcname Mopidy-Spotify

Name:           mopidy-spotify
Version:        4.0.1
Release:        1%{?dist}
Summary:        Mopidy extension for playing music from Spotify

License:        ASL 2.0
URL:            https://mopidy.com/ext/spotify/
Source0:        %{pypi_source}

ExclusiveArch:  i686 x86_64 armv7hl

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  mopidy
BuildRequires:  python3-pytest
BuildRequires:  python3-responses
BuildRequires:  python3-pyspotify
Requires:       mopidy
Requires:       python3-pyspotify


%description
Mopidy extension for playing music from Spotify.


%prep
%autosetup -n %{srcname}-%{version}
rm MANIFEST.in

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/Mopidy_Spotify-*.egg-info/
%{python3_sitelib}/mopidy_spotify/


%changelog
* Mon Dec 23 2019 Tobias Girstmair <t-rpmfusion@girst.at> - 4.0.1-1
- Initial RPM Release

