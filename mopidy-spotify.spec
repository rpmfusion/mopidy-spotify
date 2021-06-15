%global srcname Mopidy-Spotify

Name:           mopidy-spotify
Version:        4.0.1
Release:        5%{?dist}
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
* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 4.0.1-5
- Rebuild for python-3.10

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 4.0.1-2
- Rebuild for python-3.9

* Mon Dec 23 2019 Tobias Girstmair <t-rpmfusion@girst.at> - 4.0.1-1
- Initial RPM Release

